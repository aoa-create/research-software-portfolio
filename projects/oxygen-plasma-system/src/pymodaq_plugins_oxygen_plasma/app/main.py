"""GUI v1: safe bootstrap and self-check screen."""

from __future__ import annotations

import sys

from qtpy import QtCore, QtWidgets

from pymodaq_plugins_oxygen_plasma import __version__
from pymodaq_plugins_oxygen_plasma.core.bootstrap import get_bootstrap_status


class OxygenPlasmaMainWindow(QtWidgets.QMainWindow):
    """Minimal hardware-independent GUI used as the first validated checkpoint."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(f"Oxygen Plasma System — GUI v1 ({__version__})")
        self.resize(760, 430)
        self._build_ui()
        self.run_self_check()

    def _build_ui(self) -> None:
        central = QtWidgets.QWidget(self)
        self.setCentralWidget(central)
        layout = QtWidgets.QVBoxLayout(central)

        title = QtWidgets.QLabel("Oxygen Plasma System")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: 600;")
        layout.addWidget(title)

        subtitle = QtWidgets.QLabel("GUI v1 — Safe Bootstrap / Simulation Only")
        subtitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)

        form = QtWidgets.QFormLayout()
        self.version_value = QtWidgets.QLabel(__version__)
        self.mode_value = QtWidgets.QLabel()
        self.hardware_value = QtWidgets.QLabel()
        self.bypass_value = QtWidgets.QLabel()
        self.checked_value = QtWidgets.QLabel()
        form.addRow("Package version", self.version_value)
        form.addRow("Operating mode", self.mode_value)
        form.addRow("Hardware outputs", self.hardware_value)
        form.addRow("Interlock bypass", self.bypass_value)
        form.addRow("Last self-check", self.checked_value)
        layout.addLayout(form)

        self.status_box = QtWidgets.QPlainTextEdit()
        self.status_box.setReadOnly(True)
        self.status_box.setMaximumHeight(120)
        layout.addWidget(self.status_box)

        button_row = QtWidgets.QHBoxLayout()
        self.check_button = QtWidgets.QPushButton("Run Self-Check")
        self.check_button.clicked.connect(self.run_self_check)
        close_button = QtWidgets.QPushButton("Close")
        close_button.clicked.connect(self.close)
        button_row.addStretch(1)
        button_row.addWidget(self.check_button)
        button_row.addWidget(close_button)
        layout.addLayout(button_row)

        warning = QtWidgets.QLabel(
            "Safety notice: GUI v1 cannot actuate pumps, valves, MFCs, RF generators, or other hardware."
        )
        warning.setWordWrap(True)
        warning.setStyleSheet("font-weight: 600;")
        layout.addWidget(warning)

    @QtCore.Slot()
    def run_self_check(self) -> None:
        status = get_bootstrap_status()
        self.mode_value.setText("SIMULATION")
        self.hardware_value.setText("DISABLED" if not status.hardware_outputs_enabled else "ENABLED")
        self.bypass_value.setText("PROHIBITED" if not status.interlock_bypass_allowed else "ALLOWED")
        self.checked_value.setText(status.checked_at_utc)
        self.status_box.setPlainText(status.message)
        self.statusBar().showMessage("Self-check passed" if status.application_ready else "Self-check failed")


def main() -> int:
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    window = OxygenPlasmaMainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())

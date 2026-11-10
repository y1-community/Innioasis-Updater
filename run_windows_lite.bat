@echo off
rem One-line Windows launcher for the temporary Updater CE terminal session.
rem https://innioasis.app/run_windows_lite.bat
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://innioasis.app/run_windows_lite.ps1 | iex"

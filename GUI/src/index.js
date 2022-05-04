const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const url = require('url');
const path = require('path');
const os = require('os');
let miSo = os.platform();

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 1024,
        height: 768,
        resizable: false,
        webPreferences: {
            nodeIntegration: true
        }
    })
    mainWindow.loadURL('/');
};

if (miSo.toLowerCase() === 'win32') {
    app.whenReady().then(
        spawn('python', ['./main.py']),
        createWindow
    );
} else {
    // app.whenReady().then({

    // });

    console.log(miSo);
}
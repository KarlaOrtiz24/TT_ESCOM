const { app, BrowserWindow } = require('electron');
// const { spawn } = require('child_process');
const url = require('url');
const path = require('path');
const os = require('os');
// let miSo = os.platform();

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 1366,
        height: 768,
        resizable: false,
        webPreferences: {
            nodeIntegration: true
        }
    })

    let python = require('child_process').spawn(
        'py',
        ['./src/main.py']
    );

    python.stdout.on('data', function (data) {
        console.log('data: ', data.toString('utf8'));
    });

    python.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`);
    });

    mainWindow.loadURL('http://127.0.0.1:5000/');
};

app.whenReady().then(createWindow);

app.on('activate', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
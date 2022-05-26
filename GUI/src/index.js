const { app, BrowserWindow, Tray, nativeImage } = require('electron');
// const { spawn } = require('child_process');
const url = require('url');
const path = require('path');
const os = require('os');
// let miSo = os.platform();

function createWindow() {
    const mainWindow = new BrowserWindow({
        icon: './static/img/logo/KAYI-icon.png',
        width: 1366,
        height: 768,
        resizable: false,
        webPreferences: {
            nodeIntegration: true
        }
    })

    mainWindow.setMenu(null);

    mainWindow.on('closed', () => {
        app.quit();
    });

    // const icon = new Tray('./static/img/logo/KAYI-icon.png');

    console.log(icon, mainWindow);

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
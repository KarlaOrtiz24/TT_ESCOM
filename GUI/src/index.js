const { app, BrowserWindow, Tray, nativeImage } = require('electron');
const { spawn } = require('child_process');
const url = require('url');
const path = require('path');
const os = require('os');
const { dirname } = require('path');
// let miSo = os.platform();

function createWindow() {
    const mainWindow = new BrowserWindow({
        icon: __dirname + '/static/img/logo/KAYI-icon.png',
        width: 1366,
        height: 768,
        resizable: false,
        show: false,
        webPreferences: {
            nodeIntegration: true
            // preload: path.join(__dirname, 'preload.js')
        }
    })

    const splash = new BrowserWindow({
        icon: __dirname + '/static/img/logo/KAYI-icon.png',
        width: 500,
        height: 300,
        transparent: true,
        frame: false,
        alwaysOnTop: true
    });

    splash.loadFile(path.join(__dirname, '/templates/loading.html'));

    mainWindow.setMenu(null);

    mainWindow.on('closed', () => {
        app.quit();
    });

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

    setTimeout(function () {
        splash.close();
        mainWindow.show();
    }, 10000);

    // mainWindow.webContents.openDevTools();
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
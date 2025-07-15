const {app, BrowserWindow, screen, desktopCapturer, session, ipcMain} = require('electron');
const { MousePointer } = require('lucide-react');
const path = require('path');



function createWindow() {
    
    const mousePos = screen.getCursorScreenPoint();
    const currentScreen = screen.getDisplayNearestPoint(mousePos);

    const window = new BrowserWindow({
        width: 800,
        height: 600, 
        x: currentScreen.bounds.x + 100,
        y: currentScreen.bounds.y + 100,
        transparent: true,
        frame: false,
        alwaysOnTop: true,
        nodeIntegration: false,
        webPreferences: {
          preload: path.join(__dirname, '/preload.js'),
          contextIsolation: true,
        }




        
    })
    
    
    window.loadFile('index.html');
}


// Handle IPC calls from the renderer process
ipcMain.handle('get-screen-under-mouse', async () => {
    
    const mousePos = screen.getCursorScreenPoint();
    const currentScreen = screen.getDisplayNearestPoint(mousePos);
    return currentScreen;
});




ipcMain.handle('get-all-sources', async () => { 
    const sources = await desktopCapturer.getSources({ types: ['window'] });
    console.log('Available Sources:', sources);
    return sources;
});

ipcMain.handle('',) => {

}



app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});




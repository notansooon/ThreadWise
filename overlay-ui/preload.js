const {contextBridge, desktopCapturer, ipcRenderer} = require('electron');


contextBridge.exposeInMainWorld('captureStream', {

    getScreenUnderMouse: () => ipcRenderer.invoke('get-screen-under-mouse'),
    getSources: () => ipcRenderer.invoke('get-all-sources'),
    invoke:
    


});
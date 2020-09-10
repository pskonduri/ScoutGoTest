const {app, BrowserWindow} = require('electron')

function createWindow () {
    window = new BrowserWindow({width: 800, height: 600})
    window.loadFile('index.html')
}

function runInsightsServer () {
  var { PythonShell } = require('python-shell');

  let options = {
    mode: 'text'
  };
  
  PythonShell.run('./py/insights_engine_server.py', options, function (err, results) {
    if (err) throw err;
    console.log('response: ', results);

  });
}

app.on('ready', runInsightsServer)
app.on('ready', createWindow)

app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    }
})


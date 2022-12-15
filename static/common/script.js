
window.onload = function(){
    if (!('serviceWorker' in navigator)) { 
        alert('Браузер не поддерживает сервис-воркеры.') 
    }
    
    if (!('PushManager' in window)) { 
        alert('Браузер не поддерживает push-уведомления.')
    }

    return new Promise(function(resolve, reject) {
        const permissionResult = Notification.requestPermission(function(result) {
          // Поддержка устаревшей версии с функцией обратного вызова.
          resolve(result);
        });
    
        if (permissionResult) {
          permissionResult.then(resolve, reject);
        }
      })
      .then(function(permissionResult) {
        if (permissionResult !== 'granted') {
          throw new Error('Permission not granted.');
        }
      });
}

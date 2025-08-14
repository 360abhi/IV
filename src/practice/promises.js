const mypromise = new Promise((resolve,reject)=>{
    setTimeout(() => {
       const success = false
       if (success) {
        resolve("Data loaded")
       }else{
        reject("Data loading failed")
       }
    }, 1000);
})

mypromise.then((data)=>{
    console.log(data)
}).catch((error)=>{
    console.log(error)
}).finally(()=>{
    console.log("Finally block")
})
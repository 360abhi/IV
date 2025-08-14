const obj = {
    name:"Abhishek",
    greet:function(){
        setTimeout(() => {
            console.log(this.name);
        }, 1000);
    }
}

obj.greet()
function process(name,callback){
    console.log(name)
    callback()
}

function hi(){
    console.log("Hi")
}

function goodbye(){
    console.log("Good bye")
}

// process("Abhishek",hi)
// process("Ankit",goodbye)

function demo(cb){
    console.log("Step 1")
    cb()
    console.log("step 2")
}

demo(()=>console.log("Between"))
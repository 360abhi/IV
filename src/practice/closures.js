function outer(){
    const outvar = "hello this is outer var"

    return function inner(){
        console.log(outvar);
    }
}

const main = outer();
main();
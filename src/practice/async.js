async function main() {
    try {
        const user = await getUser(id);
        const orders = await getOrders(user.id);
        const products = await getProducts(orders);
        console.log(products);
    } catch (error) {
        console.error(error);
    }
}

main();

ServerEvents.tags('item', event => {
    // Get the #forge:cobblestone tag collection and add Diamond Ore to it
    event.add('c:bread_slices', 'someassemblyrequired:bread_slice')
    event.add('curios:body', '#icarus:wings')
    event.add('accessories:body', '#icarus:wings')
    event.add('c:elytra', '#icarus:wings')

    event.add('curios:bundle', 'l2backpack:arrow_bag')
    event.add('accessories:bundle', 'l2backpack:arrow_bag')

})

ServerEvents.recipes(event => {
    event.remove({ output: '#l2backpack:backpacks' })
})
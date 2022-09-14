const MORI = require('mori')
const DS_GEN = require('../source/struct-master/data-struct/data.struct.generator')
const TEST_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

test(
  `'Native'    generated list is equal to test list`,
  () => expect(DS_GEN.constructNumNList(10)).toEqual(TEST_LIST)
)

test(
  `'Mori'      generated list is equal to test list`,
  () => expect(MORI.intoArray(DS_GEN.constructNumMList(10))).toEqual(TEST_LIST)
)

test(
  `'Immutable' generated list is equal to test list`,
  () => expect(DS_GEN.constructNumIList(10).toArray()).toEqual(TEST_LIST)
)

test(
  `'Lazy'      generated list is equal to test list`,
  () => expect(DS_GEN.constructNumLList(10).toArray()).toEqual(TEST_LIST)
)

const R = require('ramda')
const MORI = require('mori')
const TEST_LIST = [3, 4, 5]
const SG_HELPER = require('../source/struct-master/bench-suite/suite.generator.helper')

test(
  `'repeatMap'     function test`,
  () => expect(SG_HELPER.repeatMap(3, [0, 1, 2], R.add(1))).toEqual(TEST_LIST)
)

test(
  `'repeatMoriMap' function test`,
  () => expect(MORI.intoArray(SG_HELPER.repeatMoriMap(3, MORI.take(3, MORI.range()), R.add(1)))).toEqual(TEST_LIST)
)

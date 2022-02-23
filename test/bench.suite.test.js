const R = require('ramda')
const MORI = require('mori')
const TEST_LIST = [3, 4, 5]
const S_GEN_HANDLER = require('../source/struct-master/bench-suite/suite.generator.handler')

test(
  `'repeatMap'     function test`,
  () => expect(S_GEN_HANDLER.repeatMap(3, [0, 1, 2], R.add(1))).toEqual(TEST_LIST)
)

test(
  `'repeatMoriMap' function test`,
  () => expect(MORI.intoArray(S_GEN_HANDLER.repeatMoriMap(3, MORI.take(3, MORI.range()), R.add(1)))).toEqual(TEST_LIST)
)

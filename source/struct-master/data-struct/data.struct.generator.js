const L = require('lazy.js')
const I = require('immutable')
const MORI = require('mori')

/**
 * @param {Number} structureSize 
 * @returns `Mori.js` **List** 
 */
const constructNumMList =
  (structureSize) =>
    MORI.take(structureSize, MORI.range())

/**
* @param {Number} structureSize 
* @returns {I.Seq} `Immutable.js` **Seq**
*/
const constructNumIList =
  (structureSize) =>
    I.Range().take(structureSize)

/**
* @param {Number} structureSize 
* @returns {Array<Number>} `Native` **Array**
*/
const constructNumNList =
  (structureSize) =>
    Array(structureSize).fill(0).map((x, i) => i)

/**
 * @param {Number} structureSize
 */
const constructNumLList =
  (structureSize) =>
    L.generate(x => x).first(structureSize)

module.exports = {
  constructNumIList,
  constructNumNList,
  constructNumMList,
  constructNumLList
}

const I = require('immutable')
const MORI = require('mori')

/**
 * @param {Number} structureSize 
 * @returns `Mori.js` **List** 
 */
const constructMoriList =
  (structureSize) =>
    MORI.take(structureSize, MORI.range())

/**
* @param {Number} structureSize 
* @returns {I.Seq} `Immutable.js` **Seq**
*/
const constructImmutableList =
  (structureSize) =>
    I.Range().take(structureSize)

/**
* @param {Number} structureSize 
* @returns {Array<Number>} `Native` **Array**
*/
const constructNativeList =
  (structureSize) =>
    Array(structureSize).fill(0).map((x, i) => i)

module.exports = {
  constructImmutableList,
  constructNativeList,
  constructMoriList
}

const I = require('immutable')
const MORI = require('mori')
const { add } = require('ramda')
const { trace } = require('../../../utils/general.helper')

/**
 * @param {Number} iterations 
 * @param {I.List|Array|ArrayLike} struct 
 * @param {Function} fnc Mapping `function`
 * @returns {I.List|Array|ArrayLike} processed `struct`
 */
const repeatMap =
  (iterations, struct, fnc) =>
    iterations > 0
      ? repeatMap(iterations - 1, struct.map(fnc), fnc)
      : struct

/**
 * Mori special repeat mapping 
 * @param {Number} iterations 
 * @param {ArrayLike} struct Mori `structure`
 * @param {Function} fnc Mapping `function`
 * @returns {ArrayLike} processed `struct`
 */
 const repeatMoriMap =
 (iterations, struct, fnc) =>
   iterations > 0
     ? repeatMoriMap(iterations - 1, MORI.map(fnc, struct), fnc)
     : struct

module.exports = {
  repeatMoriMap,
  repeatMap
}


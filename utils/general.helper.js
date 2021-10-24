const R = require('ramda')
const M = require('monet')

/**
 * Tracing function for embedding
 * @param {Object} x Traced parameter
 * @param  {...any} comments Untraced comments
 * @returns `x`
 */
const trace =
  (x, ...comments) =>
    M.IO(
      () => console.log(x, ...comments)
    ).takeRight(
      M.IO(() => x)
    ).run()

/**
 * @param {*} object 
 */
const eitherObjValuesToNumber =
  (object) =>
    R.mapObjIndexed(
      (value, key, obj) => Number(value) ? Number(value) : value,
      object
    )

/**
 * `Tab` generator: to fill the string with tabulation sequence symmetrically
 * @param {String} marker 
 */
const getTabSequence =
  (marker) =>
    R.repeat('\t', (3 - Math.round(marker.length / 8) + 2)).join('')

module.exports = {
  eitherObjValuesToNumber,
  getTabSequence,
  trace
}

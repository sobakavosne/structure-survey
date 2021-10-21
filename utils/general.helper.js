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

module.exports = {
  trace
}

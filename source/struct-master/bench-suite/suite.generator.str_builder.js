/**
 * @param {String} root 
 * @param {String} structName 
 */
const logDirBuilder =
  (root, structName) =>
    `${root}/../../log/${structName}`

/**
* @param {String} root 
* @param {String} fncName 
* @param {String} library 
* @param {Number} iterations 
* @param {Number} structSize 
* @param {String} structName 
*/
const logFileNameBuilder =
  (root, fncName, library, iterations, structSize, structName) =>
    `${root}/../../log/${structName}/{"fnc":"${fncName}","lib":"${library}","iter":${iterations},"size":${structSize}}`

module.exports = {
  logFileNameBuilder,
  logDirBuilder
}
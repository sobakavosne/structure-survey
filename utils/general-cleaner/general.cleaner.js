const FS = require('fs')

/**
 * @param {Array<String>} tmpDirs
 */
const clearTmpDirIO =
  (...tmpDirs) =>
    tmpDirs.map(tmpDir => FS.rmSync(tmpDir, { recursive: true, force: true }), () => tmpDirs)

module.exports = {
  clearTmpDirIO
}

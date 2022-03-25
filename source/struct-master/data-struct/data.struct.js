require('module-alias/register')

const H = require('@general.helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const DS_GEN = require('./data.struct.generator')

module.exports = {
  I_LIST: DS_GEN.constructNumIList(ENV.STRUCT_MAX),
  M_LIST: DS_GEN.constructNumMList(ENV.STRUCT_MAX),
  N_LIST: DS_GEN.constructNumNList(ENV.STRUCT_MAX),
  L_LIST: DS_GEN.constructNumLList(ENV.STRUCT_MAX)
}
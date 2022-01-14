const M = require('monet')

const verify = (text) =>
  M.IO(
    () => [[], ...text]
  ).bind(
    ([empty, ...destructured]) => M.IO(() => [
      empty,
      destructured.map(
        x => x === '(' || x === '[' || x === '<'
          ? empty.push(x)
          : x === ')' && empty[empty.length - 1] === '('
            || x === ']' && empty[empty.length - 1] === '['
            || x === '>' && empty[empty.length - 1] === '<'
            ? empty.pop()
            : undefined
      )
    ])
  ).bind(
    ([result, _]) => M.IO(() => result.length === 0)
  ).run()

module.export = { verify }
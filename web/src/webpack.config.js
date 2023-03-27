const path = require('path');
const fs = require('fs');
const VERSION = fs.readFileSync('../../VERSION', 'utf8');

module.exports = {
  entry: './ext/index.js',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-react']
        }
      }
    ]
  },
  output: {
    path: path.resolve(__dirname, 'static/vendors/'),
    filename: '[name].dll.js',
    chunkFilename: `renders/${VERSION}[name].js`,
    publicPath: '/static/'
  }
}

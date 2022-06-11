const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
  devServer: {
     allowedHosts: 'all',
     disable-host-check: true,
     public: 'skiffdev.gameplexsoftware.com'
};


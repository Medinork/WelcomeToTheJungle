var path = require('path');
var webpack = require('webpack');
var MiniCssExtractPlugin = require('mini-css-extract-plugin');  // Extract CSS into separate files
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = {
  entry: path.join(__dirname, 'assets/src/js/index'),
  output: {
    path: path.resolve(__dirname, 'dist'),  // Output directory
    filename: '[name].bundle.js',  // Output JavaScript file names
  },
  plugins: [
    new BundleAnalyzerPlugin(),  // For visualizing bundle size
    new MiniCssExtractPlugin({
      filename: '[name]-[hash].css',  // Output CSS files
    }),
  ],
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],  // Extract CSS using MiniCssExtractPlugin
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',  // Handle SASS files
        ],
      },
    ],
  },
  stats: 'verbose',  // Add this to get detailed stats output (optional)
};

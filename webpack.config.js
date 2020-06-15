module.exports = {
  module: {
    // this takes care of allowing babel to transpile our js code
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
};

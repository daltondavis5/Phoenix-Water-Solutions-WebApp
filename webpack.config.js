const path = require("path");

module.exports = {
  entry: "./django-project/frontend/src/index.js",
  output: {
    path: path.join(__dirname, "django-project/frontend/static/frontend"),
    filename: "main.js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
};

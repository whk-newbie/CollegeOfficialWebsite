//解决跨域问题

module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: `http://127.0.0.1:8000/api`,
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
            '/admin': {
                target: 'http://127.0.0.1:8000/admin',
                changeOrigin: true,
                pathRewrite: {
                    '^/admin': ''
                }
            }
        }
    },
};


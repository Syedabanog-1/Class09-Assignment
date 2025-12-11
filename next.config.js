/** @type {import('next').NextConfig} */
const nextConfig = {
  // Only use static export for GitHub Actions (Pages)
  output: process.env.GITHUB_ACTIONS ? 'export' : undefined,
  images: {
    unoptimized: true,
  },
  experimental: {
    logging: "verbose", // help debug any issues
  },
  // Rewrites for development and Vercel (where backend runs)
  rewrites: async () => {
    return [
      {
        source: "/api/:path*",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8001/api/:path*"
            : "/api/",
      },
      {
        source: "/docs",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8001/docs"
            : "/api/docs",
      },
      {
        source: "/openapi.json",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8001/openapi.json"
            : "/api/openapi.json",
      },
    ];
  },
};

module.exports = nextConfig;

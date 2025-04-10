# Frontend Dockerfile
FROM node:16

WORKDIR /app

# Install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy the frontend code
COPY frontend /app

# Expose the port React will run on
EXPOSE 3000

# Run the React development server
CMD ["npm", "start"]
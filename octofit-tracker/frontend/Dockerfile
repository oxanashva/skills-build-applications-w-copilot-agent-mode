# Frontend Dockerfile
FROM node:16

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the frontend code
COPY . /app

# Expose the port React will run on
EXPOSE 3000

# Run the React development server
CMD ["npm", "start"]
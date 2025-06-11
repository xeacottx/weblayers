# -------- Build Stage --------
FROM node:18 AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Set API URL to backend service within Kubernetes
ENV REACT_APP_API_URL=http://backend.weblayers.svc.cluster.local:8000
RUN npm run build

# -------- Production Stage --------
FROM nginx:alpine

# Copy the built React app
COPY --from=build /app/build /usr/share/nginx/html

# Overwrite default.conf with your nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
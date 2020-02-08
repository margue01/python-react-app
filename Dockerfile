# Frontend files
FROM node:12.15 as build-deps

WORKDIR /usr/src/ui-people
COPY ui-people/package.json ui-people/yarn.lock ./
RUN yarn install
COPY ui-people/ ./
RUN yarn build

# Service app
FROM python:3

WORKDIR /usr/src/app
COPY --from=build-deps /usr/src/ui-people ./ui-people

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh ./
COPY setup.py ./
COPY app_people/ ./app_people
COPY data ./data

EXPOSE 8003

CMD ["./run.sh"]

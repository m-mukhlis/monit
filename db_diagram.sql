CREATE TABLE "users" (
  "id" int PRIMARY KEY,
  "full_name" varchar,
  "created_at" timestamp
);

CREATE TABLE "wallets" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "balance" int,
  "created_at" datetime DEFAULT (now()),
  "last_edit" datetime
);

CREATE TABLE "transactions" (
  "id" int PRIMARY KEY,
  "wallet_id" int UNIQUE NOT NULL,
  "transaction_type" varchar,
  "created_at" varchar,
  "status" varchar
);

CREATE TABLE "recipients" (
  "id" int PRIMARY KEY,
  "transaction_id" int,
  "recipient" varchar,
  "amount" int
);

ALTER TABLE "users" ADD FOREIGN KEY ("id") REFERENCES "wallets" ("user_id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("wallet_id") REFERENCES "wallets" ("id");

ALTER TABLE "recipients" ADD FOREIGN KEY ("transaction_id") REFERENCES "transactions" ("id");

CREATE INDEX "product_status" ON "wallets" ("balance");

CREATE UNIQUE INDEX ON "wallets" ("id");

COMMENT ON COLUMN "transactions"."created_at" IS 'When transaction created';

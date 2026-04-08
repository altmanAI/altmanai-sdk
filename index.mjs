import { createReceipt, emitEvent, hashArtifact, verifyArtifact } from "@altmanai/core";

const payload = { product: "DailyPilot", action: "artifact.created" };
const expectedHash = hashArtifact(payload);

const receipt = createReceipt({
  type: "artifact.created",
  actor: "DailyPilot",
  summary: "Generated planning artifact",
  source: "node-basic-example",
});

const event = emitEvent({
  name: "receipt.generated",
  source: "node-basic-example",
  payload: receipt,
});

console.log({ receipt, event, verification: verifyArtifact(payload, expectedHash) });

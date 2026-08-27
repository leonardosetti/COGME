import type { SimulationResult } from "@/lib/simulation";

export type SavedSimulation = SimulationResult & {
  id: string;
  createdAt: string;
};

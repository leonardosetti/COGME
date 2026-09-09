import SimulationForm from "@/components/SimulationForm";
import InternationalTransferOffers from "@/components/InternationalTransferOffers";

export default function SimulationsPage() {
  return <><header className="page-header"><div><div className="eyebrow">Ferramenta de cálculo</div><h1>Nova simulação</h1><p>Compare seu recebimento internacional com transparência.</p></div></header><SimulationForm /><InternationalTransferOffers /></>;
}

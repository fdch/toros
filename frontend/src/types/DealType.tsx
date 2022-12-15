type DealType = {
    deal_id: bigint
    date: Date
    company_id: bigint
    funding_amount?: number
    funding_round: string
}

export default DealType;
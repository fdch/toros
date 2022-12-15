type CompanyType = {
    company_id: bigint,
    founding_date: Date,
    name: string,
    country?: string,
    description?: string,
}

export default CompanyType;
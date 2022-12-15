import { useEffect, useState } from "react";
import Deal from '../types/DealType';
import Service from '../types/Service';

export interface AllDeals {
    results: Deal[];
}


const useGetDealService = (company_id: bigint) => {
    const [result, setResult] = useState<Service<AllDeals>>({
        status: 'loading'
    });
    useEffect(() => {
        fetch(`http://localhost:20002/deals_by_company/${company_id}`)
            .then(response => response.json())
            .then(response => {
                console.log(response);
                setResult({ status: 'loaded', payload: response })
            })
            .catch(error => setResult({ status: 'error', error }));
    }, [company_id]);

    return result;

}

export default useGetDealService;
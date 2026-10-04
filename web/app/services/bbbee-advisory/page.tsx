import ServiceCategoryPage from '@/components/ServiceCategoryPage'
import { servicePages } from '@/util/servicePages'

export const metadata = {
    title: 'B-BBEE Advisory | Knowescape Consulting',
    description: servicePages['bbbee-advisory'].introduction,
}

export default function BBBEEAdvisoryPage() {
    return <ServiceCategoryPage service={servicePages['bbbee-advisory']} />
}

import ServiceCategoryPage from '@/components/ServiceCategoryPage'
import { servicePages } from '@/util/servicePages'

export const metadata = {
    title: 'Startup Support | Knowescape Consulting',
    description: servicePages['startup-support'].introduction,
}

export default function StartupSupportPage() {
    return <ServiceCategoryPage service={servicePages['startup-support']} />
}

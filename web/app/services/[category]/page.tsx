import type { Metadata } from 'next'
import { notFound, redirect } from 'next/navigation'
import ServiceCategoryPage from '@/components/ServiceCategoryPage'
import { serviceAliases, servicePages, type ServiceCategory } from '@/util/servicePages'

type PageProps = {
    params: Promise<{ category: string }>
}

export function generateStaticParams() {
    return Object.keys(servicePages).map((category) => ({ category }))
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
    const { category } = await params
    const alias = serviceAliases[category]
    const service = servicePages[category as ServiceCategory]
        ?? (alias ? servicePages[alias.category] : undefined)

    if (!service) {
        return { title: 'Service not found | Knowescape Consulting' }
    }

    return {
        title: `${service.title} | Knowescape Consulting`,
        description: service.introduction,
    }
}

export default async function ServicePage({ params }: PageProps) {
    const { category } = await params
    const service = servicePages[category as ServiceCategory]

    if (service) return <ServiceCategoryPage service={service} />

    const alias = serviceAliases[category]
    if (alias) redirect(`/services/${alias.category}#${alias.section}`)

    notFound()
}

import '../../styles/landing.css'
import ContactSection from '@/components/ContactSection';

export default function Contact() {
	return (
		<>
			<header id="contact">
				<div className="contact-container">
					<h1 className='site-heading'>
						Contact <span>Us</span>
					</h1>
				</div>
			</header>
			<ContactSection />
		</>
	);
}

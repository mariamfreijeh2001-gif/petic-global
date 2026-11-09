/** Site-wide constants: identity, contact details, navigation and shared lists. */

export const site = {
  name: 'PETIC GLOBAL',
  url: 'https://petic-global.com',
  tagline: 'Construction, infrastructure, agriculture and oil & gas across the Gulf States and East Africa.',
  quote: 'Chase the vision, not the money. The money will end up following you.',
  phone: '+974 4418 8100',
  phoneRaw: '+97444188100',
  email: 'info@petic-global.com',
  salesEmail: 'sales@petic-global.com',
  ceoEmail: 'ceo@petic-global.com',
  address:
    'Office No. 1503, 15th Floor, Building No. 24, Al-Nasr Tower (A), Street 950, West Bay, Zone 60, P.O. Box 5090, Doha, Qatar',
  mapCoords: '25.312882047721047,51.51902880080558',
  city: 'Doha, Qatar',
  tanzaniaAddress: 'Kisutu Street 2423, Dar es Salaam, Tanzania',
  profile: '/Petic-International-Business-Profile.pdf',
  social: {
    facebook: '#',
    instagram: '#',
    x: '#',
    linkedin: '#',
  },
} as const;

export interface NavItem {
  href: string;
  label: string;
  children?: NavItem[];
}

export const activities: NavItem[] = [
  { href: '/agriculture/', label: 'Agriculture' },
  { href: '/roads-construction/', label: 'Roads Construction' },
  { href: '/civil-works-and-construction/', label: 'Civil Works & Construction' },
  { href: '/oil-and-gas/', label: 'Oil & Gas' },
];

export const nav: NavItem[] = [
  { href: '/', label: 'Home' },
  { href: '/about/', label: 'About Us' },
  { href: '/our-activities/', label: 'Our Activities', children: activities },
  { href: '/contact/', label: 'Contact Us' },
];

export const partners = [
  { file: 'partner-almaha.jpg', name: 'Almaha for Industry' },
  { file: 'partner-linex.jpg', name: 'LINE-X' },
  { file: 'partner-petro-sharq.jpg', name: 'Petro Sharq Group' },
  { file: 'partner-teamone.jpg', name: 'TeamOne Shipping & Clearing' },
  { file: 'partner-nature-petroleum.jpg', name: 'Nature for Petroleum, Gas and Minerals' },
];

export const generalServices = [
  'Cost estimating',
  'Pre-construction services',
  'Historic restoration',
  'Infrastructure solutions',
  'General contractor',
  'Industrial engineering',
];

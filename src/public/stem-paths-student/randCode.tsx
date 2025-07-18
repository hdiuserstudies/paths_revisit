import React, { useState } from 'react';

const generateRandomCode = (length: number): string => {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let result = '';
  const charactersLength = characters.length;

  for (let i = 0; i < length; i += 1) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }

  return result;
};

const RandCode: React.FC = () => {
  const [code] = useState<string>(() => generateRandomCode(8)); // default 8-character code

  return (
    <div className="p-4 rounded-xl shadow-md bg-white w-fit">
      <h2 className="text-xl font-semibold mb-2">{code}</h2>
    </div>
  );
};

export default RandCode;

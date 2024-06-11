<template>
    <div class="flex flex-col">
        <div class="w-[30] text-gray-900 flex justify-center">
            <div class="m-0 sm:m-10 bg-white sm:rounded-lg flex justify-center flex-1">
                <div class="w-full md:w-auto xl:w-5/12 p-6 sm:p-12">
                    <Persona></Persona>
            </div>
        </div>
    </div>
        <div class="mt-12 w-full">
            <TablePersonas></TablePersonas>
        </div>
    </div>
</template>

<script>
    import Persona from '../../components/Persona.vue'
    import TablePersonas from '../../components/TablePersonas.vue';

    export default{
        components:
            {
                Persona,
                TablePersonas,
            }
    }
</script>